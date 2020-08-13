#!/bin/bash
Recipient=”itodebasya@gmail.com”
Subject=”Greeting”
Message=”Welcome”
`mutt -s $Subject $Recipient <<< $Message`
