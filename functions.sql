-- Func 1:search contacts by partern
CREATE OR REPLACE FUNCTION search_contacts(pattern_text TEXT)
RETURNS TABLE(id INT, username VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.username, p.phone
    FROM phonebook p
    WHERE p.username ILIKE '%' || pattern_text || '%'
       OR p.phone ILIKE '%' || pattern_text || '%';
END;
$$ LANGUAGE plpgsql;


-- Func 2:get contacts with pagination
CREATE OR REPLACE FUNCTION get_contacts_paginated(limit_value INT, offset_value INT)
RETURNS TABLE(id INT, username VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.username, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT limit_value OFFSET offset_value;
END;
$$ LANGUAGE plpgsql;