<?php
function generate_reset_token($username) {
  $time = intval(microtime(true) * 1000);
  echo "Before md5: \n";
  echo ($username . $time . "\n");
  $token = md5($username . $time);
  return $token;
}

// Example usage:
$username = "htbadmin";
$reset_token = generate_reset_token($username);
echo "Reset Token: " . $reset_token;
?>
