            function call_registerend(e)
            {
            	//alert('got it')
            	//e.preventDefault()
                var new_user_req = new XMLHttpRequest()
                        
                new_user_req.open('POST', '/api/register_end')
                new_user_req.setRequestHeader("Content-type", "application/json")
                var fname = document.getElementById('firstname').value
                var lname = document.getElementById('lastname').value
                var uname = document.getElementById('username').value
                var pass  = document.getElementById('password').value
                var bio   = document.getElementById('biodata').value
                var postVars = JSON.stringify({firstname:fname,lastname:lname,username:uname,password:pass,biodata:bio})
                new_user_req.send(postVars)


        	   new_user_req.onreadystatechange = function()
                {
                    if (new_user_req.readyState == 4 && new_user_req.status == 200)
                    {                  
                        var response = JSON.parse(new_user_req.responseText);
                        //alert(response)
                        document.getElementById('response').innerHTML = response.response;
                        if(response.code == 1){
                        	window.location.href="/login.html";
                        }      
                    }
                }
                
                return false
            }
            function test(e){
            	alert('Yeathinking rght!');
            	e.preventDefault();
            	return false;
            }