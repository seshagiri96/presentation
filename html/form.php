<?php

	$email = $_POST['email'];
	$message = $_POST['user_message'];

	echo "Form Successfully Submitted by<br>";
	echo $_POST['email']."<br>";
	echo $_POST['user_message']."<br>";

	// user credentials
	$servername = "localhost";
	$username = "username";
	$password = "password";
	$db = "mydb";

	$conn = new mysqli($servername,$username,$password,$db);

	

	if ($conn->connect_error) {
    	die("Connection failed: " . $conn->connect_error);
	} 
	echo "Connected successfully to ".$db."<br>";

	$instr = "INSERT INTO comments(email,message) VALUES ($email,$message)";
	//$instr = "SELECT * FROM comments";
	if($conn->query($instr)){
		echo "Query Successful";
	}else {
		echo "query unsuccessful";
	}

	echo "<---End--->";//$result;
	//echo $result;

	// if(result->num_rows >0){
	// 	while($row=$result->fetch_assoc()){
	// 		//echo $row["email"];
	// 	}
	// }
?>