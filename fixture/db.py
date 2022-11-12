import MySQLdb

from model.group import Group


class DbFixture():
    def __init__(self, host, name, user, password):
        self.name = name
        self.host = host
        self.user = user
        self.password = password
        self.connection = MySQLdb.connect(host=host, database=name, user=user, password=password)

    def get_group_list(self):
        lst = []
        curs = self.connection.cursor()
        try:
            curs.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in curs:
                (id, name, header, footer) = row
                lst.append(Group(name, header, footer))
        finally:
            curs.close()
        return lst

    def destroy(self):
        self.connection.close()