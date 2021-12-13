

class Teams:

    @staticmethod
    def show_all():
        return 'select * from teams;', []

    @staticmethod
    def select():
        team_name = input('Enter team name:')
        sport_type = input('Enter sport type:')
        return "select * from teams where team_name = %s and sport_name = %s;", [team_name, sport_type]

    @staticmethod
    def delete():
        team_name = input('Enter team name:')
        sport_type = input('Enter sport type:')
        return "delete from teams where team_name = %s and sport_name = %s;", [team_name, sport_type]

    @staticmethod
    def insert():
        team_name = input('Enter team name:')
        sport_name = input('Enter sport name:')
        members_count = input('Enter members count:')
        return "insert into teams (team_name, sport_name, members_count) VALUES (%s, %s, %s)", \
               [team_name, sport_name, members_count]

    @staticmethod
    def update():
        team_name = input('Enter team name:')
        sport_name = input('Enter sport name:')
        members_count = input('Enter members count:')
        return "update teams set members_count = %s " \
               "where team_name = %s and sport_name = %s;", [members_count, team_name, sport_name]