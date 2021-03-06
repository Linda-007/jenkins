from apptest.apppo.page.app import App


class TestContact:
    def setup_class(self):
        self.app = App().start()

    def setup(self):
        self.main = self.app.goto_main()

    def teardown_class(self):
        self.app.stop()
    def test_addcontact(self):
        name = "Linda"
        phonenumber = "13567899876"
        editpage = self.mian.goto_addresslist().click_addcontact().addcontact_menual().edit_contact()
        editpage.edit_contact(name,phonenumber)
        editpage.verify_ok()

    def test_delcontact(self):
        name = "RT"

        delpage = self.main.goto_searchpage().click_personhome().edit_person().del_person(). alertpage().search_contact()
        delpage.search_contact(name)