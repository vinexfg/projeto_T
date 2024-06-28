#abstração


class Log:
    def log(self, msg):
        raise  NotImplementedError('Implemente o metodo log')
    

if __name__ == '__main__':
    l = Log()
    l.log('qualquer coisa')


