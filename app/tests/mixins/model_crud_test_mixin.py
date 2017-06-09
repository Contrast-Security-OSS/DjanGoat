

class ModelCrudTests(object):
    """Mixin for testing CRUD functionality of models.
        self.model is the model created locally and saved to the database
        self.model_update_attribute is the string name of the attribute of the model being tested for update
        self.model_update_input is the new value that model_update_attribute is being set to
        self.parent is the model's parent object, to which it has a foreign key and a cascade on delete
            self.parent is None if the object has no parent
    """
    def setUp(self):
        print("\nI ran!\n")

    def test_create_model(self):
        """
            Makes sure the model was created and put in the database
        """
        self.assertNotEqual(self._get_from_db(self.model), None)

    def test_read_model(self):
        """
            Makes sure that the model can be read from the database by comparing the two objects primary keys
        """
        self.assertEqual(self._get_from_db(self.model), self.model)

    def test_update_model(self):
        """
            Makes sure the model can be updated in the database by doing the following steps:
            1. Sets the attribute of the local model
            2. Saves the change to the database
            3. Updates the db_model from the database
            4. Asserts that the changed attribute is the same in the local model and the database model
        """
        setattr(self.model, self.model_update_attribute, self.model_update_input)
        self.model.save()
        self.assertEqual(
            getattr(self.model, self.model_update_attribute),
            getattr(self._get_from_db(self.model), self.model_update_attribute)
        )

    def test_delete_model(self):
        response = self.model.delete()
        num_objects_deleted = response[0]
        # 1 object deleted from database
        self.assertEqual(num_objects_deleted, 1)

        # PTO with primary key matching the deleted pto's primary key no longer in database
        self.assertEqual(self._get_from_db(self.model), None)

    def test_delete_user_and_pto(self):
        """Test to ensure Model is deleted when its parent is deleted.
        """
        if self.parent is not None:
            response = self.parent.delete()
            num_objects_deleted = response[0]
            '''2 objects deleted from database'''
            self.assertEqual(num_objects_deleted, 2)

            self.assertIsNone(self._get_from_db(self.parent), "Parent not deleted from the database")
            self.assertIsNone(self._get_from_db(self.model), "Model not deleted from database with cascade")
        else:
            pass

    @staticmethod
    def _get_from_db(model):
        """Helper method to get the model from the database"""
        return model.__class__.objects.filter(pk=model.pk).first()
