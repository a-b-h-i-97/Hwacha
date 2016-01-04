import mock
import pytest
from ..Hwacha.appControl import appControl
from ..Hwacha.appControl.socialMediaControl import socialMediaControl

def test_isInSmList():
    appObject = appControl.appController()
    smObject = socialMediaControl.socialMediaController()
    retAdd = smObject.addSm(['twitter','facebook'])
    retValue = appObject.isInSmList('facebook')
    assert retValue == True

def test_isInSmList2():
    appObject = appControl.appController()
    smObject = socialMediaControl.socialMediaController()
    retAdd = smObject.addSm(['twitter','facebook'])
    retValue = appObject.isInSmList(['wrong'])
    assert retValue == False





def test_addSm():
    appObject = appControl.appController()
    retValue = appObject.addSm('Mail')
    assert retValue == True

def test_getAvailableSmList():
    smObject = socialMediaControl.socialMediaController()
    appObject = appControl.appController()
    retValue = appObject.getAvailableSmList()
    assert retValue == smObject.displaySm()

    
def test_removeSm():
    sm_object = mock.Mock()
    sm_object.rmSm = mock.MagicMock(return_value = True)
    
    original = appControl.socialMediaControl.socialMediaController
    appControl.socialMediaControl.socialMediaController = sm_object 
    
    app_object = appControl.appController()
    value = app_object.removeSm(['twitter'])
#    sm_object.rmSm.assert_called_with(['twitter'])
    assert value == True
    appControl.socialMediaControl.socialMediaController = original

