# Opti-School
Description: Tools that are beneficial to students in college

## cold email
### Structure
An automated email sending toolkit 
- **tools components**
    - **`load_db`**: where you specify recipients ("email", "firstName lastName")
    - **`models`**: where your db methods are specified
    - **`send_email`**: where you configure the mime and smtp and make the email sending
    - **`visualization`**: a pie viewchart of failure/success sending rate

- **assets components**
    - **`template.txt`**: where <content> are meant to be replaced
### Instructions

## drive-backup (Google)
### Structure
An automated workflow (via github action) for repo push and backup notes into google drive

- **backup_script**: 
    - components: authentication(), upload_file(), upload_folder()
    - task: perform current working directory copying into a google service account accessible shared drive by folder_id

- **.github/workflow/push_drive-sync.yml**
    - components: cron job, image loading, dependency install, commit-push, python backup_script.py
### Instructions
