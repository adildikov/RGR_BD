

class SportTypes:

    @staticmethod
    def show_all():
        return 'select * from sport_types;', []

    @staticmethod
    def select():
        sport = input('Enter sport type:')
        return "select * from sport_types where sport_name = %s;", [sport]

    @staticmethod
    def delete():
        sport = input('Enter sport type:')
        return "delete from sport_types where sport_name = %s;", [sport]

    @staticmethod
    def insert():
        sport_name = input('Enter sport name:')
        description = input('Enter description:')
        rules = input('Enter rules:')
        return "insert into sport_types (sport_name, description, rules) VALUES (%s, %s, %s)", \
               [sport_name, description, rules]

    @staticmethod
    def update():
        sport_name = input('Enter sport name:')
        description = input('Enter description:')
        rules = input('Enter rules:')
        return "update sport_types set description = %s, rules = %s where sport_name = %s",\
               [description, rules, sport_name]