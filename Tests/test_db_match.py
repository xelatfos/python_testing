import allure


@allure.suite("Internal testing")
@allure.sub_suite("Testing DB connection")
def test_group_list(app, db):
    db_lst = db.get_group_list()
    assert len(db_lst)>0