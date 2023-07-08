from django import forms


class HeadingForm(forms.Form):
    url = forms.URLField(label="URL", max_length=200, required=True)

    options = [("ol", "Ordered"), ("ul", "Unorderd"), ("p", "Custom")]
    choice = forms.ChoiceField(
        label="Type",
        choices=options,
        initial="ol",
        widget=forms.RadioSelect(),
        # widget=forms.RadioSelect(attrs={"onclick": "check()"}),  # Add attribute  
        required=True,
    )
    mark = forms.CharField(label="Mark", max_length=1, required=False)
    # mark = forms.CharField(widget=forms.HiddenInput(), required=False)      # Hidden field for mark
    # headings_text = forms.CharField(
    #     label="Ouput",
    #     help_text="Shows output with headings",
    #     widget=forms.Textarea(attrs={"rows": 10, "cols": 20, "readonly": "readonly"}), required=False
    # )
