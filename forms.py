"""Forms for playlist app."""

from wtforms import SelectField
from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from models import db, Playlist, Song

BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

class PlaylistForm(ModelForm):
    """Form for adding playlists."""

    class Meta:
        model = Playlist
    

class SongForm(ModelForm):
    """Form for adding songs."""

    class Meta:
        model = Song


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
