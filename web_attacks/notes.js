//1. resetPassword() code found:
//<script>
        function resetPassword() {
            if ($("#new_password").val() == $("#confirm_new_password").val()) {
                $("#error_string").html('');
                fetch(`/api.php/token/${$.cookie("uid")}`, {
                    method: 'GET'
                }).then(function(response) {
                    return response.json();
                }).then(function(json) {
                    fetch(`/reset.php`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'
                        },
                        body: `uid=${$.cookie("uid")}&token=${json['token']}&password=${$("#new_password").val()}`
                    }).then(function(response) {
                        return response.text();
                    }).then(function(res) {
                        $("#error_string").html(res);
                    });
                });
            } else {
                $("#error_string").html('Passwords do not match!');
            }
        };
//    </script>
    
// 2. Cookie: PHPSESSID=sgr7ld75gouudgmgh8ibqd4r7i; uid=74

// 3. Found Administrator {"uid":"52","username":"a.corrales","full_name":"Amor Corrales","company":"Administrator"}{"token":"e51a85fa-17ac-11ec-8e51-e78234eb7b0c"}
