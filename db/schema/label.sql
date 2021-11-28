create table label
(
    label_id    int auto_increment
        primary key,
    name        varchar(255) not null,
    description varchar(255) null,
    constraint label_id_uindex
        unique (label_id),
    constraint label_name_uindex
        unique (name)
);

INSERT INTO annotator.label (label_id, name, description) VALUES (0, 'o', null);
INSERT INTO annotator.label (label_id, name, description) VALUES (1, 'ip', null);
INSERT INTO annotator.label (label_id, name, description) VALUES (2, 'hash', null);
INSERT INTO annotator.label (label_id, name, description) VALUES (3, 'url', null);
INSERT INTO annotator.label (label_id, name, description) VALUES (4, 'domain', null);
INSERT INTO annotator.label (label_id, name, description) VALUES (5, 'group', null);
INSERT INTO annotator.label (label_id, name, description) VALUES (6, 'malware', null);
INSERT INTO annotator.label (label_id, name, description) VALUES (7, 'email', null);
INSERT INTO annotator.label (label_id, name, description) VALUES (8, 'filename', null);
