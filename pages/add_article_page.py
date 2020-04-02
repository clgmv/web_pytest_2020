from common.base import Base

class AddArticlePage(Base):
    '''新增文章分类'''
    art_cate_loc = ('css','#left-side>ul>li:nth-child(11)>a')    #定位文章分类导航标签
    add_arc_cate_loc = ('xpath','//div[@id="content-block"]/div/div[2]/div/a')    #定位增加文章分类按钮
    cate_input_loc = ('id','id_n')     #定位分类输入框
    pre_loc = ('xpath','//*[@id="articleclassify_form"]/div[2]/button')     #定位保存按钮
    all_table = ('xpath','//table')



    def click_art_cate(self):
        '''点击文章分类导航标签'''
        self.click(self.art_cate_loc)

    def edit_classify(self,text):
        '''编辑文章分类'''
        self.click(self.add_arc_cate_loc)
        self.send(self.cate_input_loc,text=text)
        self.click(self.pre_loc)
        #self.finds()   复数定位

    def is_addarticle_success(self,text):
        '''判断新增文章是否成功，返回true和false'''
        table = self.get_text(self.all_table)
        return text in table