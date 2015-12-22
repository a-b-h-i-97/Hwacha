
# Test for broadcast

from ..broadcast import broadcast #path set
import pytest
import random
import mock
from mock import Mock
import tweepy

# def test_broadcst():
#     key={'twitter':{'consumer_key':'igjX6vqB8HtMzPByguX9KUtqv',
#      'consumer_secret': 'R8pyvLiKSDDTjyf84DnKVgM4IQLYTXq9fDdCbsq3vCEzXkC7qz',
#      'access_token': '4472517314-QveTAuRwPQ0JKnBTkVobZZTG3KusZm8fFBUSXKw',
#      'access_token_secret':'XItUgPH1VCP027HufEewBqdO45dCEz4Ga4IwqOmgo2brN',
#       }}
#     soc_media= ['twitter']
#     error_code = None
#     message='Hello Hwacha'+str(random.random()) # random message
#     push = broadcast.broadcastmessage(message,soc_media,key) 
#     assert push['twitter'] == error_code





def test_twitter_auth():
    mock_oauthhandler = mock.Mock()
    mock_API = mock.Mock()
    mock_api = mock.Mock()
    mock_auth = mock.Mock()

    original_oauthhandler = tweepy.OAuthHandler
    original_API = tweepy.API
    tweepy.OAuthHandler = mock_oauthhandler
    tweepy.API = mock_API

    mock_oauthhandler.return_value = mock_auth
    mock_API.return_value = mock_api
    
    t = broadcast.TwitterBroadcast("test_consumer_key", 
                "test_consumer_secret", 
                "test_access_token",
                "test_access_token_secret")

    ret = t.authentication()
    tweepy.OAuthHandler.assert_called_with("test_consumer_key", "test_consumer_secret")
    mock_auth.set_access_token.assert_called_with("test_access_token", "test_access_token_secret")
    tweepy.API.assert_called_with(mock_auth)
    assert ret == mock_api
    
    tweepy.OAuthHandler = original_oauthhandler
    tweepy.API = original_API







# def test_broadcst2():

#     wrong_key ={'twitter': {'consumer_key':'qB8HtMzPByguX9KUtqv',
#      'consumer_secret': 'R8pyvLiKSDDTjyf84DnKVgM4IQLYTXq9fDdCbsq3vCEzXkC7qz',
#      'access_token': '44725173veTAuRwPQ0JKnBTkVobZZTG3KusZm8fFBUSXKw',
#      'access_token_secret':'tUgPH1VCP027HufEewBqdO45dCEz4Ga4IwqOmgo2brN'
#      }}
#     soc_media= ['twitter']
#     error_code = 89
    
#     push = broadcast.broadcastmessage('Hello Hwach',soc_media,wrong_key)
#     print push
#     assert push['twitter']== error_code 


# This test is timing out for unknown reason
#def test_mailBroadcast2():
#	key = {'mail':{'subject':'Test Subject', 'to':'userHwacha@gmail.com', 'consumer_key':'senderHwacha@gmail.com', 'consumer_secret':'wrongPass123'}}
#	soc_media = ['mail']
#	code = "Authentication failed"

#	push_return = broadcast.broadcastmessage('Hello',soc_media,key)
#	print push_return
#       assert push_return['mail'] == code




def test_mailBroadcast():
    mock_server = Mock()
    mock_subject = Mock()
    mock_to = Mock()
    mock_sender = Mock()
    mock_pass = Mock()
    mailObject = broadcast.mailBroadcast(mock_subject, mock_to, mock_sender, mock_pass)
    retAuthValue = mailObject.authentication(mock_server)
    assert retAuthValue == "success"
    mock_server.login.assert_called_with(mock_sender, mock_pass)
    retPushValue = mailObject.push("hello",mock_server)
    assert retPushValue == "success"
    assert mock_server.ehlo.called
    assert mock_server.starttls.called

def test_mailBroadcast_auth_failure():
    mock_server = Mock()
    mock_subject = Mock()
    mock_to = Mock()
    mock_sender = Mock()
    mock_pass = Mock()
    mailObject = broadcast.mailBroadcast(mock_subject, mock_to, mock_sender, mock_pass)
    retAuthValue =mailObject.authentication(mock_server)
    #with pytest.raises(broadcast.AuthenticationError):
     #   assert retAuthValue == "failure"
	
    
def test_authentication():
    mock = Mock()
    mock.authentication()
    mock.return_value = "True"
    mock.authentication.assert_called_with()

    

