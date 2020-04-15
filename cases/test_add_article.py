import pytest
from pages.add_article_page import AddArticlePage
from common.read_yml import readyml

d = readyml(r'E:\web_pytest_2020\cases\testdata.yml')
testdata = d['test_add_param_article']

class Test_add_article():
     def test_add_article(self,login):
          '''测试添加文章分类'''
          driver = login
          add_article = AddArticlePage(driver)
          add_article.click_art_cate()
          add_article.edit_classify('selenium测试')
          res = add_article.is_addarticle_success('selenium测试')
          print('编辑是否成功:%s'%res)
          assert res


     @pytest.mark.parametrize('test_input,excepted',testdata)
     def test_add_param_article(self,login,test_input,excepted):
          '''用例描述：1，先登录 2，点文章分类导航标签 3，编辑页面输入，分类名称 4，点击保存按钮'''
          driver = login
          add_article = AddArticlePage(driver)
          add_article.click_art_cate()
          add_article.edit_classify(test_input)
          res = add_article.is_addarticle_success(test_input)
          print('实际结果是:%s' % res,'期望结果是:%s' % excepted)
          assert res == excepted

