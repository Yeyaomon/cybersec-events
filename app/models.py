from . import db

class Data(db.Model):
    __tablename__ = 'data'
    event_id = db.Column('EventID', db.String, primary_key=True)
    source_ip = db.Column('SourceIP', db.String)
    destination_ip = db.Column('DestinationIP', db.String)
    attack_type = db.Column('AttackType', db.String)
    attack_severity = db.Column('AttackSeverity', db.String)
    
    # One to One response
    response = db.relationship(
        'Response', 
        back_populates='data', 
        uselist=False,
        primaryjoin="Data.event_id==Response.event_id"
    )

class Response(db.Model):
    __tablename__ = 'response'
    event_id = db.Column(
        'EventID', db.String,
        db.ForeignKey('data.EventID'),
        primary_key=True
    )
    attack_type = db.Column('AttackType', db.String)
    data_exfiltrated = db.Column('DataExfiltrated', db.String)
    threat_intelligence = db.Column('ThreatIntelligence', db.Text)
    response_action = db.Column('ResponseAction', db.String)
    data = db.relationship(
        'Data',
        back_populates='response',
        primaryjoin="Response.event_id==Data.event_id"
    )
