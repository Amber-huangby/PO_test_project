from page_object.index import Index


class Test_add_member():

    def test_1(self):
        driver = Index().go_to_add_member()
        driver.add_member_mesg()
        assert driver.get_first_name() == 'aa'
