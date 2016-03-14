#!/usr/bin/env python
from __future__ import division
from __future__ import division
import mysql.connector
import sys

__author__ = 'youval.dar'

__doc__ = """
Move data in and out of MySQL
"""

class MysqlReadWrite(object):
    """
    Move data in and out of MySQL
    Working on a single table in a singel database
    """

    def __init__(self,connection_config,tb_name):
        """
        Setup the connection
        Args:
            connection_config (dict): connection configuration in the form:
                config = {
                  'user': 'xxx',
                  'password': 'yyy',
                  'host': 'xxx.xxx.xxx.xxx',
                  'database': 'db_name'
            tb_name (str): the MySQL table name
        }
        """
        self.config = connection_config
        try:
            self.cnx = mysql.connector.connect(**self.config)
            self.cursor = self.cnx.cursor()
            # Set a flag indicating that connection is open -> remember to close it...
            self.connection_open = True
        except mysql.connector.Error as err:
            print "Failed creating database: %s" % str(err)
            exit(1)
        self.tb_name = tb_name
        self.db_name = self.config['database']

    def close_connection(self):
        """
        Close connection
        """
        self.cursor.close()
        self.cnx.close()


    def push_data_to_mysql(self,col_names,data,close_when_done=True, delete_existing=True):
        """
        Move data to Tableau MySql

        Args:
            tb_name (str): the MySQL table name
            col_names (list): list of column names
            data (list): list of tuples of the data
            delete_existing (bool): When True, delete all data in table
            close_when_done (bool): close connection when done

        """
        if bool(data):
            # Delete all existing data
            if delete_existing:
                del_cmd = 'delete from %s' % self.tb_name
                self.cursor.execute(del_cmd)
            #
            k = '(' + ','.join(col_names) + ')'
            add_new_data = "INSERT INTO %s %s VALUES (" % (self.tb_name,k)
            add_new_data += ','.join(['%s'] * len(data[0])) + ')'
            # turn the data to strings
            data = [map(str,x) for x in data]
            self.cursor.executemany(add_new_data,data)
            if close_when_done:
                self.cnx.commit()
                self.close_connection()

    def read_data_to_list(self,query=None,close_when_done=True, test_query_data_size=True):
        """
        Execute query and and return the data in a list

        Args:
            query (str): the query string.
            close_when_done (bool): close connection when done
            test_query_data_size (bool): make sure the data is no larger than 10^6 records
                                         works only if we have no more than one 'where' condition in this version

        Returns:
            data (list): list containing the data
            tb_col_names (list): list containing columns names

        Query string example:
            '''\
            SELECT *
            FROM db_name.table_name'''
        """
        if not bool(query):
            query = 'SELECT * FROM %s.%s' % (self.db_name, self.tb_name)

        desc_str = 'DESCRIBE  %s.%s' % (self.db_name, self.tb_name)
        self.cursor.execute(desc_str)
        tb_col_names = [str(x[0]) for x in self.cursor.fetchall()]

        # make sure the table is not to large
        count_str = 'SELECT count(*) FROM  %s.%s' % (self.db_name, self.tb_name)
        if test_query_data_size:
            if 'where' in query.lower():
                where_list = query.lower().split('where')
                if len(where_list) > 2:
                    print >> sys.stderr, "\nThis version does not support more than one 'WHERE' condition\n"
                    exit(-1)
                else:
                    count_str += ' WHERE %s' % where_list[-1]
            self.cursor.execute(count_str)
            cnt = self.cursor.fetchall()
            if len(cnt) != 1:
                print >> sys.stderr, "\nError counting the query number of rows\n"
                exit(-1)
            cnt = int(list(cnt[0])[0])
            if cnt > 1e6:
                print >> sys.stderr, "\nThis method is limited to import 10^6 lines\n"
                exit(-1)


        # execute the SQL query using execute() method.
        self.cursor.execute(query)
        # fetch all of the rows from the query
        data = self.cursor.fetchall()

        if close_when_done:
                self.cnx.commit()
                self.close_connection()

        return data, tb_col_names
