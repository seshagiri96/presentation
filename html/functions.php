<?php
	function insert($email, $message, $conn){
		$instr = "INSERT INTO `comments` (`email`,`message`) VALUES ('$email','$message')";

		if($conn->exec($instr)){
			echo "Query Successful<br>";
		}else {
			echo "Query unsuccessful<br>";
		}
	}

	function pnt($conn){
		$instr = "SELECT * FROM `comments`";

		$result = $conn->exec($instr);
		if($result->num_rows > 0){
			while ($row = $result->fetch_assoc()){
				echo $row['email'],$row['message'];
			}
		}
	}

?>