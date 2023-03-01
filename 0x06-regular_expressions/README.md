# [0x06. Regular expression]()

## Background context

	For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

	Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

		#!/usr/bin/env ruby
		puts ARGV[0].scan(/127.0.0.[0-9]/).join

## Mandatory Tasks

### 0. [Simply matching School]()

	The regular expression must match School

### 1. [Repetition token #0]()

### 2. [Repetition token #1]()

### 3. [Repetition token #2]()

### 4. [Repetition token #3]()

### 5. [Not quite HBTN yet]()

Requirements:

	The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between

### 6. [Call me maybe]()

	This task is brought to you by a professional advisor Neha Jain, Senior Software Engineer at LinkedIn.

	Requirement:

	The regular expression must match a 10 digit phone number

### 7. [OMG WHY ARE YOU SHOUTING]()

	Requirement:

	The regular expression must be only matching: capital letters

## Advanced tasks

### 8. [Text me]()

	This exercise was prepared for you by Guillaume Plessis, VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project on Twitter.

	For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

	Requirements:

	Your script should output: [SENDER],[RECEIVER],[FLAGS]
	The sender phone number or name (including country code if present)
	The receiver phone number or name (including country code if present)
	The flags that were used
