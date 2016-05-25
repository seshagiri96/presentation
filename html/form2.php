<?php

	$email = $_POST['email'];
	$message = $_POST['user_message'];

	echo "Form Successfully Submitted by<br>";
	echo $_POST['email']."<br>";
	echo $_POST['user_message']."<br>";

	include 'login_info.php';

	$servername = $user['servername'];
	$username   = $user['username'];
	$password 	= $user['password'];
	$db 		= "mydb";
		
	try {
	    $conn = new PDO("mysql:host=$servername;dbname=$db", $username, $password);
	    // set the PDO error mode to exception
	    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	    echo "Connected successfully"; 
	}
	catch(PDOException $e){
	    echo "Connection failed: " . $e->getMessage();
	}

	
	include 'functions.php';
	insert($email,$message,$conn);

	pnt($conn);
	echo "<-- End -->";

	$conn = null;
?>