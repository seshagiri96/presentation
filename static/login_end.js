function call_loginend(e)
            {
            	//alert('jds')
            	//e.preventDefault()
                var req = new XMLHttpRequest()
                        
                req.open('POST', '/api/login_end')
                req.setRequestHeader("Content-type", "application/json")
                var un = document.getElementById('username').value
                var pwd = document.getElementById('password').value
                var postVars = JSON.stringify({username:un,password:pwd})
                req.send(postVars)
                //req.send();

        	   req.onreadystatechange = function()
                {
                    if (req.readyState == 4 && req.status == 200)
                    {                  
                        var response = JSON.parse(req.responseText)
                        document.getElementById('response').innerHTML = response.response
                        if(response.code ==1){
                            //alert('hello');
                        	window.location.href='/profile.html';
                        }
                    }
                }
                
                return false
            }
