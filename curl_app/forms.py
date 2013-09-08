import re

from django import forms



class MainForm(forms.Form):
	urlField = forms.CharField(max_length=250)
	urlField.widget.attrs.update({'placeholder' : 'Enter your URL here...'})
	urlField.widget.attrs.update({'class' : 'input-xxlarge'})
	# validate(form_url)

	def is_valid(self):
		form = super(MainForm, self).is_valid()
		if not form:
			return form
		pattern = re.compile(r'^(http|https|www)(://|\.)(\S+)$',re.IGNORECASE)
		match = re.match(pattern,self.cleaned_data['urlField'])
		if match:
			return True
		else:
			self._errors['urlField'] = 'URL is invalid'
		
		# form = super(MainForm, self).is_valid()
		# if not form:
		# 	return form
		
		# pattern = re.compile(r'^((http://www)+?|(www)+?).(\w*).(\S*)$')
		# match = re.match(pattern,self.cleaned_data['urlField'])
		# if match:
		# 	return True
		# else:
		# 	self._errors['invalid_url'] = 'URL is invalid'
			

		