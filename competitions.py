

class Competitions:

    @staticmethod
    def show_all():
        return 'select * from competitions;', []

    @staticmethod
    def select():
        date = input('Enter competition date:')
        name = input('Enter competition name:')
        return "select * from competitions where competition_name = %s and competition_date = %s;", [name, date]

    @staticmethod
    def delete():
        date = input('Enter competition date:')
        name = input('Enter competition name:')
        return "delete from competitions where competition_name = %s and competition_date = %s;", [name, date]

    @staticmethod
    def insert():
        competition_date = input('Enter competition date:')
        level = input('Enter competition level:')
        competition_name = input('Enter competition name:')
        sport_name = input('Enter sport name:')
        return "insert into competitions (competition_date, level, competition_name, sport_name)" \
               "VALUES (%s, %s, %s, %s)", [competition_date, level, competition_name, sport_name]

    @staticmethod
    def update():
        competition_date = input('Enter competition date:')
        level = input('Enter competition level:')
        competition_name = input('Enter competition name:')
        sport_name = input('Enter sport name:')
        return "update competitions set level = %s where competition_date = %s and competition_name = %s" \
               " and sport_name = %s;", [level, competition_date, competition_name, sport_name]
