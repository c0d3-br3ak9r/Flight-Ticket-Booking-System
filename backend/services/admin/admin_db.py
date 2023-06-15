from models.db import DB

class AdminDB(DB):

    create_admin_table = '''
                            CREATE TABLE IF NOT EXISTS `admin_users` (
                                `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                `username` TEXT NOT NULL UNIQUE,
                                `password` TEXT NOT NULL
                            )
                            '''

    create_admin_session_table = '''
                                CREATE TABLE IF NOT EXISTS `admin_session` (
                                    `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                    `admin_id` INTEGER NOT NULL UNIQUE,
                                    `session_key` TEXT NOT NULL UNIQUE,
                                    `expires_at` DATETIME NOT NULL,
                                    CONSTRAINT `sess_admin_id_fk` 
                                    FOREIGN KEY (`admin_id`) REFERENCES `admin_users` (`id`) ON DELETE CASCADE
                                )
                                '''    


    def __init__(self):
        super().__init__()
        self._exec(self.create_admin_table)
        self._exec(self.create_admin_session_table)


    ''' Create a new admin user '''
    def create_admin(self, username, password):
        query = ''' INSERT INTO `admin_users` (`username`, `password`) VALUES (?, ?) '''
        return self._exec(query, [username, password])


    ''' Get the hashed password of the admin user based on username '''
    def get_admin_password(self, username):
        query = "SELECT `id`, `password` FROM `admin_users` WHERE `username`=?"
        if ( self._exec(query, [username]) ):
            return self.cursor.fetchone()
        return 0
    

    ''' Checks whether there already exists a session with same key '''
    def session_exists(self, session_key):
        query = "SELECT `expires_at` FROM `admin_session` WHERE `session_key`=?"
        if ( self._exec(query, [session_key]) ):
            return self.cursor.fetchone()
        return 0
    

    ''' Delete session key if the user already has session '''
    def delete_session(self, session_key):
        query = "DELETE FROM `admin_session` WHERE `session_key`=?"
        return self._exec(query, [session_key])
    

    ''' Remove session key if the user already has session '''
    def delete_session_by_id(self, user_id):
        query = "DELETE FROM `admin_session` WHERE `admin_id`=?"
        return self._exec(query, [user_id])


    ''' Creates a new admin session with session key and expires at as 24hr interval '''
    def create_session(self, user_id, session_key, expires_at):
        query = '''INSERT INTO `admin_session` (`admin_id`, `session_key`, `expires_at`)
                VALUES (?, ?, ?)'''
        return self._exec(query, [user_id, session_key, expires_at])


    def __del__(self):
        return super().__del__()