# Timeline

Timeline is an aplication for manage project schedules.

First we have 3 type of users:

- **Admin/Leader:** Is in charge of manage all projects and see all project status.

- **Account Manager:** Is allowed to generate reports from all developers.

- **Developer:** Is allowed to manage project in charge of them, create schedules and manage their task status.

Then we have the following models.

## Project

A project is a model represented by a real project, this model is in charge of save all te informarion about the project.

The main idea is that all the information about the project (important documentas and documentation) will be saved in this entity.

## Schedule type

This model represents the type of development to practice.

For example.

- Adjusment.

- Requirements.

- Meeting.

- Layers.

- ...

## Schedule

A schedule is a model represented by a real schedule, its representas the amout of time to take for a developer for do somthing (according to the schedule type).

## Task

A task is a something little thing to do and its can take a time or can be programmable, like an reminder.

These tasks will have only a description and a human readable identifier.
