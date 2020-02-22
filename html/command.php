<?php
#$user_name=$_SERVER['PHP_AUTH_USER'];
#$password=$_SERVER['PHP_AUTH_PW'];
$address = "127.0.0.1";
$service_port = 1025;
$c = $_GET['command'];
$log = "";
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === false) {
    $log .= "socket_create() failed: reason: " . socket_strerror(socket_last_error()) . "\n";
} 
else {
    $log.= "socket created\n";
	$log.= "Attempting to connect to '$address' on port '$service_port'...";
	$result = socket_connect($socket, $address, $service_port);
	if ($result === false) {
    	$log.="socket_connect() failed.\nReason: ($result) " . socket_strerror(socket_last_error($socket)) . "\n";
	} 
	else {
    	$log.= "OK.\n";
		$out = '';
		$in = json_encode($c)."\r\n";
		socket_write($socket, $in, strlen($in));
		$log.= "Reading response:\n\n";
		$out = socket_read($socket, 2048);
		$log.= $out;
		$log.= "Closing socket...";
		socket_close($socket);
		$log.= "OK.\n\n";
	}
}
print(json_encode($c));
print(json_encode($log));
?>