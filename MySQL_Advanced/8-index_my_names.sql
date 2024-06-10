-- index on name and first char of name


CREATE INDEX idx_name_first ON names (name(1));
