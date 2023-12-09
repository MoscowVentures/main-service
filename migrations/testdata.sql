insert into app.themes (uuid, title) values 
('uuid1', 'theme1'),
('uuid2', 'theme2'),
('uuid3', 'theme3');

insert into app.stories (text, image_url) values 
('text1', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fru%2F%25D1%2584%25D0%25BE%25D1%2582%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D1%2584%25D0%25B8%25D0%25B8%2F%25D0%25BF%25D1%2580%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B4%25D0%25B0&psig=AOvVaw3I2i0vdQpgNMZ47B71EOPr&ust=1702125087135000&source=images&cd=vfe&ved=0CBIQjRxqFwoTCJCK75rs_4IDFQAAAAAdAAAAABAE'), 
('text2', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fru%2F%25D1%2584%25D0%25BE%25D1%2582%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D1%2584%25D0%25B8%25D0%25B8%2F%25D0%25BF%25D1%2580%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B4%25D0%25B0&psig=AOvVaw3I2i0vdQpgNMZ47B71EOPr&ust=1702125087135000&source=images&cd=vfe&ved=0CBIQjRxqFwoTCJCK75rs_4IDFQAAAAAdAAAAABAE'), 
('text3', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fru%2F%25D1%2584%25D0%25BE%25D1%2582%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D1%2584%25D0%25B8%25D0%25B8%2F%25D0%25BF%25D1%2580%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B4%25D0%25B0&psig=AOvVaw3I2i0vdQpgNMZ47B71EOPr&ust=1702125087135000&source=images&cd=vfe&ved=0CBIQjRxqFwoTCJCK75rs_4IDFQAAAAAdAAAAABAE');

insert into app.question_types (
  id, title
) values (
  1, 'single'
);

insert into app.questions (
  question_type, content, right_answers, level, age, theme_uuid
) values (
  1, '{"title":"Question?", "answers":["answer1", "answer2", "answer3"]}', '{}', 3, 12, 'uuid1'
), (
  1, '{"title":"Question?", "answers":["answer1", "answer2", "answer3"]}', '{}', 3, 12, 'uuid1'
), (
  1, '{"title":"Question?", "answers":["answer1", "answer2", "answer3"]}', '{}', 3, 12, 'uuid1'
), (
  1, '{"title":"Question?", "answers":["answer1", "answer2", "answer3"]}', '{}', 3, 12, 'uuid1'
), (
  1, '{"title":"Question?", "answers":["answer1", "answer2", "answer3"]}', '{}', 3, 12, 'uuid1'
), (
  1, '{"title":"Question?", "answers":["answer1", "answer2", "answer3"]}', '{}', 3, 12, 'uuid1'
), (
  1, '{"title":"Question?", "answers":["answer1", "answer2", "answer3"]}', '{}', 3, 12, 'uuid1'
);