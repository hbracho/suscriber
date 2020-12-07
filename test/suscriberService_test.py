import sys
sys.path.append("..")
import unittest
from mock import Mock,patch,MagicMock
from src.domain.suscriberService import SuscriberService


class SuscriberServiceTest(unittest.TestCase):
    
    def test_searchAll_OK(self):
        mockRepository = Mock()
        suscriberService = SuscriberService(mockRepository)
        suscriberService.searchAll()
        mockRepository.getAll.assert_called_with()
    
    @patch('src.application.utils.check_password')
    def test_searchByTopicName_sucessed(self, mock_check_password):
        
        mock_check_password.return_value=True

        mockRepository = MagicMock()
        suscriber = {'topic_name': 'orderCreate', 'key': '123123123'}
        mockRepository.searchByTopic.return_value(suscriber)

        suscriberService = SuscriberService(mockRepository)
        topic_name='OrderCreated'
        key='1234'
        result = suscriberService.searchByTopicName(topic_name,key)
        assert result == suscriber
        
    
    # def test_searchByTopicName_errorKeyIncorrect(self):
    #     mockRepository = Mock()
    #     suscriberService = SuscriberService(mockRepository)
    #     suscriberService.searchAll()
    #     mockRepository.getAll.assert_called_with()
    
    # def test_searchByTopicName_errorTopicNotFound(self):
    #     mockRepository = Mock()
    #     suscriberService = SuscriberService(mockRepository)
    #     suscriberService.searchAll()
    #     mockRepository.getAll.assert_called_with()
    


if __name__ == '__main__':
    unittest.main()