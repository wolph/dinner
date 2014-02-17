class KoornbeursRouter(object):
    '''
    A router to control all database operations on models in the Koornbeurs
    application.
    '''
    def db_for_read(self, model, **hints):
        '''
        Attempts to read koornbeurs models go to koornbeurs.
        '''
        if model._meta.app_label == 'koornbeurs':
            return 'koornbeurs'
        return None

    def db_for_write(self, model, **hints):
        '''
        Attempts to write koornbeurs models go to koornbeurs.
        '''
        if model._meta.app_label == 'koornbeurs':
            return 'koornbeurs'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        '''
        Allow relations if a model in the koornbeurs app is involved.
        '''
        if obj1._meta.app_label == 'koornbeurs' and \
           obj2._meta.app_label == 'koornbeurs':
           return True
        return None

    def allow_migrate(self, db, model):
        '''
        Make sure the koornbeurs app only appears in the 'koornbeurs'
        database.
        '''
        if db == 'koornbeurs':
            return model._meta.app_label == 'koornbeurs'
        elif model._meta.app_label == 'koornbeurs':
            return False
        return None
