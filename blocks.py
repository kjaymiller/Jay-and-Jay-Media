from jinja import Markup

def quote_form(default_text):
    text = f'''
	<div class="jumbotron">

	<h3>Request a Quote</h3>

	<form name="contact" method="POST" data-netlify="true">
	  <div class="form-group">
	    <label class="col-sm-2">Your Name: <input style="width:250px;" type="text" name="name" /></label>   
	  </div>

	  <div class="form-group">
	    <label class="col-sm-2">Your Email: <input style="width:250px;"  type="email" name="email" /></label>
	  </div>

	  <div class="form-group">
	    <label class="col-sm-2">
            Message: 
            <textarea style="width:250px;" name="message"> 
              {default_text}
            </textarea>
            </label>
	  </div>

	  <div class="form-group">
	    <button class="btn btn-dark" type="submit">Send</button>
	  </div>
          </form>'''

    return Markup(text)
