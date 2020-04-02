from common.base import Base
from common.config import host


login_url = host+'/xadmin/'
class Loginpage(Base):
      '''登陆页面'''
      user_loc = ('id','id_username')
      psw_loc = ('id','id_password')
      login_button_loc = ('xpath','//button')

      #判断页面元素
      judge_loc = ('css','#top-nav>div>a')
      #// a[1][@class ='navbar-brand']
      def input_user(self,username):
            self.send(self.user_loc,username)

      def input_psw(self,password):
            self.send(self.psw_loc,password)

      def click_button(self):
            self.click(self.login_button_loc)

      def login(self,username='admin',password='yoyo123456'):
            self.driver.get(login_url)
            self.input_user(username)
            self.input_psw(password)
            self.click_button()

      def is_login_success(self):
            '''判断是否登录成功'''
            text = self.get_text(self.judge_loc)
            print('登陆完成后，获取到文本%s'%text)
            return text=='后台页面'
if __name__ == '__main__':
      from selenium import webdriver
      driver = webdriver.Chrome()
      web = Loginpage(driver)
      web.login()
      result = web.is_login_success()
      print(result)
      driver.quit()