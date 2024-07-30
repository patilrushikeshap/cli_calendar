from sqlalchemy import create_engine, Column, Integer, String, Time, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

class Meeting(Base):
    __tablename__ = 'meetings'
    id = Column(Integer, primary_key=True)
    day = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    room = Column(String(50))
    participants = Column(String)

engine = create_engine('sqlite:///meetings.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def schedule_meeting(day, start_time, end_time, room=None, participants=None):
    start_time = datetime.strptime(start_time, '%H:%M').time()
    end_time = datetime.strptime(end_time, '%H:%M').time()
    day = datetime.strptime(day, '%Y-%m-%d').date()
    participants_list = participants.split(",") if participants else []

    # Check for collisions
    meetings = session.query(Meeting).filter_by(day=day).all()
    for meeting in meetings:
        if (start_time < meeting.end_time) and (end_time > meeting.start_time):
            if room and meeting.room == room:
                return "Meeting collision detected: Room is occupied!"
            meeting_participants = meeting.participants.split(",") if meeting.participants else []
            if any(participant in participants_list for participant in meeting_participants):
                return f"Meeting collision detected: Participant(s) {set(participants_list) & set(meeting_participants)} are unavailable!"

    # Schedule the meeting
    new_meeting = Meeting(day=day, start_time=start_time, end_time=end_time, room=room, participants=participants)
    session.add(new_meeting)
    session.commit()
    return "Meeting scheduled successfully!"

def list_meetings():
    meetings = session.query(Meeting).all()
    return meetings

import sys

def print_meetings():
    meetings = list_meetings()
    for meeting in meetings:
        print(f"Day: {meeting.day}, Start Time: {meeting.start_time}, End Time: {meeting.end_time}, Room: {meeting.room}, Participants: {meeting.participants}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python calendar_system.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'schedule':
        if len(sys.argv) != 7:
            print("Usage: python calendar_system.py schedule <day> <start_time> <end_time> <room> <participants>")
            sys.exit(1)
        day = sys.argv[2]
        start_time = sys.argv[3]
        end_time = sys.argv[4]
        room = sys.argv[5]
        participants = sys.argv[6]
        print(schedule_meeting(day, start_time, end_time, room, participants))
    elif command == 'list':
        print_meetings()
    else:
        print("Unknown command")
