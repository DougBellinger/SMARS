<?php
#$user_name=$_SERVER['PHP_AUTH_USER'];
#$password=$_SERVER['PHP_AUTH_PW'];
$c = $_GET['command'];
print(json_encode($c));
?>