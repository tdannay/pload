import csv
import time

reader1 = csv.DictReader(open('F19LAW.csv', 'r'))

#fieldnames = ['netID', 'lastname', 'firstname', 'barcode', 'psoftID', 'projlevel', 'gender', 'birthdate', 'email']
writer = open('output.csv', 'w')

for row in reader1:
	x = row['Ext Sys ID'].lower()
	y_last = row['Last']
	y_first = row['First Name']
	line = row['ID'] + "," + row['Career'] + "," + row['Prim Prog'] + "," + row['Strt Level'] + "," + row['Birthdate'] + "," + row['Email']
	reader2 = csv.DictReader(open('onecard.csv', 'r'))
	for row in reader2:
		if x == row['NetID']:
			writer.write(row['NetID'] + "," + row['Last Name'] + "," + row['First Name'] + "," + row['Magstripe'] + "," + line)
			writer.write('\n')
			break
	else:
		writer.write(x + "," + y_last + "," + y_first + ",," + line)
		writer.write('\n')


######


writer.close()

reader3 = csv.reader(open('output.csv', 'r'), delimiter=',')
writer2 = open('sisload.xml', 'w')

writer2.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?> \n")
writer2.write("<users> \n")

for row in reader3:
	netID = row[0]
	lastName = row[1]
	firstName = row[2]
	barcode = row[3]
	psoftID = row[4]

	career = row[5]
	academicPlan = row[6]
	level = row[7]
	if career == "LAW":
		if academicPlan == "LJD3D":
			if level == "P1":
				expirationDate = "2022-08-01"
			elif level == "P2":
				expirationDate = "2021-08-01"
			elif level == "P3":
				expirationDate = "2020-08-01"
			else:
				expirationDate = "2020-08-01"
		elif academicPlan == "LJD4E":
			if level == "P1":
				expirationDate = "2023-08-01"
			elif level == "P2":
				expirationDate = "2022-08-01"
			elif level == "P3":
				expirationDate = "2021-08-01"
			elif level == "P4":
				expirationDate = "2020-08-01"
			else:
				expirationDate = "2020-08-01"
	elif career == "LAWND":
		expirationDate = "2019-12-31"
	elif career == "SJD":
		expirationDate = "2020-08-01"
	elif career == "USLEG" or "LHMSJ" or "INSUR" or "LIPIG" or "ENENV":
		if level == "P1":
			expirationDate = "2021-08-01"
		elif level == "P2":
			expirationDate = "2020-08-01"
		else:
			expirationDate = "2020-08-01"
	else:
		expirationDate = "2020-08-01"

	#gender = row[8]
	#if gender == "M":
	#	gender = "MALE"
	#elif gender == "F":
	#	gender = "FEMALE"
	#else:
	#	gender = ""

	dateOfBirth = row[8]
	
	try:
		conv = time.strptime(dateOfBirth, "%m/%d/%Y")
		dateOfBirth = time.strftime("%Y-%m-%d", conv)
	except ValueError:
		dateOfBirth = ""

	emailAddress = row[9]

	writer2.write("	<user> \n")
	writer2.write("		<record_type desc=\"Public\">PUBLIC</record_type> \n")
	writer2.write("		<primary_id>" + netID + "</primary_id> \n")
	writer2.write("		<first_name>" + firstName + "</first_name> \n")
	writer2.write("		<middle_name></middle_name> \n")
	writer2.write("		<last_name>" + lastName + "</last_name> \n")
	writer2.write("		<full_name>" + firstName + " " + lastName + "</full_name> \n")
	writer2.write("		<pin_number></pin_number> \n")
	writer2.write("		<user_title desc=\"\"></user_title> \n")
	writer2.write("		<job_category desc=\"\"></job_category> \n")
	writer2.write("		<job_description></job_description> \n")

	#writer2.write("		<gender desc=\"" + gender.capitalize() + "\">" + gender + "</gender> \n")
	writer2.write("		<gender></gender> \n")
	
	writer2.write("		<user_group desc=\"Grad Law\">GRADLAW</user_group> \n")
	writer2.write("		<campus_code desc=\"\"/> \n")
	writer2.write("		<web_site_url></web_site_url> \n")
	writer2.write("		<cataloger_level desc=\"[00] Default Level\">00</cataloger_level> \n")
	writer2.write("		<preferred_language desc=\"English\">en</preferred_language> \n")
	writer2.write("		<birth_date>" + dateOfBirth + "</birth_date> \n")
	writer2.write("		<expiry_date>" + expirationDate + "</expiry_date> \n")
	writer2.write("		<purge_date>" + expirationDate + "</purge_date> \n")
	writer2.write("		<account_type desc=\"External\">EXTERNAL</account_type> \n")
	writer2.write("		<external_id>SIS</external_id> \n")
	writer2.write("		<password></password> \n")
	writer2.write("		<force_password_change></force_password_change> \n")
	writer2.write("		<status desc=\"Active\">ACTIVE</status> \n")
	writer2.write("		<contact_info> \n")
	writer2.write("			<addresses /> \n")
	writer2.write("			<emails> \n")
	writer2.write("				<email preferred=\"true\" segment_type=\"External\"> \n")
	writer2.write("					<email_address>" + emailAddress + "</email_address> \n")
	writer2.write("					<email_types> \n")
	writer2.write("						<email_type desc=\"School\">school</email_type> \n")
	writer2.write("					</email_types> \n")
	writer2.write("				</email> \n")
	writer2.write("			</emails> \n")
	writer2.write("			<phones /> \n")
	writer2.write("		</contact_info> \n")
	writer2.write("		<user_identifiers> \n")
	if barcode != "":
		writer2.write("			<user_identifier segment_type=\"External\"> \n")
		writer2.write("				<id_type desc=\"Barcode\">BARCODE</id_type> \n")
		writer2.write("				<value>" + barcode + "</value> \n")
		writer2.write("				<status>ACTIVE</status> \n")
		writer2.write("			</user_identifier> \n")
	else:
		pass
	writer2.write("			<user_identifier segment_type=\"External\"> \n")
	writer2.write("				<id_type desc=\"Additional ID 1\">OTHER_ID_1</id_type> \n")
	writer2.write("				<value>" + psoftID + "</value> \n")
	writer2.write("				<status>ACTIVE</status> \n")
	writer2.write("			</user_identifier> \n")
	writer2.write("		</user_identifiers> \n")
	writer2.write("	</user> \n")

writer2.write("</users> \n")