from models.db import DB

class UserDB(DB):

    create_user_table = '''
                            CREATE TABLE IF NOT EXISTS `users` (
                                `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                `username` TEXT NOT NULL UNIQUE,
                                `password` TEXT NOT NULL
                            )
                            '''


    create_user_session_table = '''
                                CREATE TABLE IF NOT EXISTS `user_session` (
                                    `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                    `user_id` INTEGER NOT NULL UNIQUE,
                                    `session_key` TEXT NOT NULL UNIQUE,
                                    `expires_at` DATETIME NOT NULL,
                                    CONSTRAINT `sess_user_id_fk` 
                                    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE
                                )
                                '''


    def __init__(self):
        super().__init__()
        self._exec(self.create_user_table)
        self._exec(self.create_user_session_table)


    ''' Create a new user '''
    def create_user(self, username, password):
        query = ''' INSERT INTO `users` (`username`, `password`) VALUES (?, ?) '''
        return self._exec(query, [username, password])


    ''' Get the hashed password of the user based on username '''
    def get_user_password(self, username):
        query = "SELECT `id`, `password` FROM `users` WHERE `username`=?"
        if ( self._exec(query, [username]) ):
            return self.cursor.fetchone()
        return 0
    

    ''' Get user id and expires at if there already exists a session with same key '''
    def get_user_id_expires(self, session_key):
        query = "SELECT `user_id`, `expires_at` FROM `user_session` WHERE `session_key`=?"
        if ( self._exec(query, [session_key]) ):
            return self.cursor.fetchone()
        return 0
    

    ''' Delete session key if the user already has session '''
    def delete_session(self, session_id):
        query = "DELETE FROM `user_session` WHERE `session_key`=?"
        return self._exec(query, [session_id])
    

    ''' Remove session key if the user already has session '''
    def delete_session_by_id(self, user_id):
        query = "DELETE FROM `user_session` WHERE `user_id`=?"
        return self._exec(query, [user_id])


    ''' Creates a new user session with session key and expires at as 24hr interval '''
    def create_session(self, user_id, session_key, expires_at):
        query = '''INSERT INTO `user_session` (`user_id`, `session_key`, `expires_at`)
                VALUES (?, ?, ?)'''
        return self._exec(query, [user_id, session_key, expires_at])
    

    def __del__(self):
        return super().__del__()