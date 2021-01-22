from src.main_page import MainPage


class TestAddMember():
    def setup_class(self):

        self.main = MainPage()

    def test_add_member(self):
        #main = MainPage()
        #1.首页跳转添加成员页面，2.添加成员，3.获取成员信息
        self.result = self.main.go_to_add_member().add_member().get_member_list()
        print(self.result)
        assert '皮2' in self.result

    def test_add_depar(self):
        self.result = self.main.go_to_contact().go_to_dep().add_depar().get_depar_list()
        print(self.result)
        assert '质量保障' in self.result

    def teardown_class(self):
        self.main.driver.close()
        self.main.driver.quite()
