<?php 
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    file_put_contents('test.txt', file_get_contents('php://input'));
}
?>