# Design

			     	Hawcha UI
		       		   /\
                      /  \      
                     /    \
                    /      \
           AppControl   Authentication
               /\            \
              /  \            \
             /    \            \
            /      \            \
          SMC	  Broadcast     User





###AppControl:

	getSmName()
		Input: None
		Output: Social Media name
		Specification: Read social media name from user.
		
	getSmUserName()
		Input: None
		Output:	Social media user name
		Specification: Read social media user name from user. 

	getSmUserPasswd()
		Input: None
		Output: Social media password
		Specification: Read social media password from user


	getMessage()
		Input: None
		Output: Message to broadcast
		Specification: Read the message from the user

	getSmList()
		Input: None
		Output: List of social media 
		Specification: Read the list of social media to broadcast from user.

	isInSmList()
		Input: Social media name.
		Output: Boolean
		Specification: check if input social media is in social media list 

###Authentification:

	getUserName()
		Input: None
		Output: User name
		Specification: Read the user name from user

	getUserPasswd()
		Input: None
		Output: Password
		Specification: Read the password from the user

###SMC:

	addSm()
		Input: getSmName(),getSmUserName(), getSmUserPasswd()
		Output: Boolean
		Specification: Add the given social media.
		
	rmSm()
		Input: getSmName()
		Output: Boolean
		Specification: Remove the given social media.
		
	displaySm()	
		Input: None
		Output: Social media list
		Specification:	Display the list of social media

	countSm()
		Input: None
		Output: Number of social media
		Specification: Count the number of social medias in the social media list

	isSmAvailable()
		Input: getSmName()
		Output: Boolean
		Specification: Checks if the given social media is in the social media list


###Broadcast:

	broadcastMessage()
		Input: getMessage(), getSmList() 
		Output: Boolean
		Specification: Broadcast the message to various social media

###User:

	addUser()
		Input: getUserName(), getUserPasswd() 
		Output: Boolean
		Specification: Add application user.
		
	rmUser()
		Input: getUserName(), getUserPasswd()
		Output: Boolean
		Specification: Remove user from the application
