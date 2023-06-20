import pytest


# class
# function
# encapsulation
# object
# constructor

# inheritance


# pytesthtml  pytest-html
# allure report

class TestPet():
    # Class is a collection of functions\methods and variables

    @pytest.mark.parametrize('status', ['available'])
    def test_get_pet_by_status(self, status, libs, apis):
        '''
        :param status: Status needs to validate
        :return: nothing
        '''
        print("i m in test")
        resp = libs.get_pet(apis.GET_PET_BY_STATUS.format(status))
        for record in resp:
            assert record[
                       'status'] == status, "status is not correct for id {} status should be available but showing {}"\
                .format(
                record["id"], record["status"])

    @pytest.mark.parametrize('tag_name', ['string'])
    def test_pet_by_tags(self, tag_name, libs, apis):

        resp = libs.get_pet(url=apis.GET_PET_BY_TAGS)
        for record in resp:
            assert record[
                       'tags'][0][
                       'name'] == tag_name, "status is not correct for id {} tag should be {} but showing {}".format(
                tag_name, record["id"], record["tags"][0]['name'])

    def test_create_pet(self, libs):
        status = "sold"
        resp = libs.create_pet(name="executing_from_test", status=status)
        assert resp['status'] == status


    @pytest.mark.parametrize('status', ['available'])
    def test_verify_pet_end_to_end_scenario(self, status, libs, apis):
        '''
        :param status: Status needs to validate
        :return: nothing
        '''
        status = "available"
        resp = libs.create_pet(name="executing_from_test", status=status)
        pet_id = resp['id']

        resp = libs.get_pet_by_id(pet_id)
        assert resp[
                   'status'] == status, "status is not correct for id {} status should be available but showing {}".\
            format(
            resp["id"], resp["status"])
        assert pet_id == resp['id']

