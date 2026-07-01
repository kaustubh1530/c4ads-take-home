from django.test import TestCase
from django.urls import reverse
from .models import Entity

class EntityAPITests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create test data — does NOT touch your real DB
        Entity.objects.create(
            id=101, name="Test Person A", country="Russia",
            entity_type="Individual", date_added="2022-01-01",
            program="RUSSIA-EO14024", notes="Test note"
        )
        Entity.objects.create(
            id=102, name="Test Org B", country="Russia",
            entity_type="Organization", date_added="2022-02-01",
            program="RUSSIA-EO14024", notes="Test note"
        )
        Entity.objects.create(
            id=103, name="Test Person C", country="Iran",
            entity_type="Individual", date_added="2021-05-10",
            program="IRAN-EO13599", notes="Test note"
        )
        Entity.objects.create(
            id=104, name="Test Org D", country="China",
            entity_type="Organization", date_added="2020-09-15",
            program="DPRK-EO13722", notes="Test note"
        )

    def test_get_all_entities_returns_200(self):
        """GET /api/entities/ should return 200 and all records"""
        response = self.client.get('/api/entities/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 4)

    def test_filter_by_country(self):
        """Filtering by country returns only matching records"""
        response = self.client.get('/api/entities/?country=Russia')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        for entity in data:
            self.assertEqual(entity['country'], 'Russia')

    def test_filter_by_entity_type(self):
        """Filtering by entity_type returns only matching records"""
        response = self.client.get('/api/entities/?entity_type=Individual')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        for entity in data:
            self.assertEqual(entity['entity_type'], 'Individual')

    def test_filter_by_country_and_entity_type(self):
        """Combining both filters returns the correct subset"""
        response = self.client.get('/api/entities/?country=Russia&entity_type=Individual')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Test Person A')

    def test_filter_no_results(self):
        """Filters with no match return empty list"""
        response = self.client.get('/api/entities/?country=Brazil&entity_type=Individual')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])