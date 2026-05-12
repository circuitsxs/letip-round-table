from django.db import models

# ANNOUNCEMENT MODEL
# Creates a database table for portal announcements


class Announcement(models.Model):
    # each field below corresponds to a column in the database table
    # SHORT TITLE FOR THE ANNOUNCEMENT
    title = models.CharField(max_length=100)

    # MAIN ANNOUNCEMENT MESSAGE / BODY TEXT
    # This allows longer text than CharField above
    message = models.TextField()

    # AUTOMATICALLY STORES DATE/TIME WHEN THE ANNOUNCEMENT IS CREATED
    date_posted = models.DateTimeField(auto_now_add=True)

    # CONTROLS HOW THE OBJECT APPEARS INSIDE DJANGO ADMIN PANEL
    def __str__(self):
        return self.title