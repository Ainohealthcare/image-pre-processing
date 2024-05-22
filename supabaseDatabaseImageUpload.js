const fs = require("fs");
const path = require("path");

const { createClient } = require("@supabase/supabase-js");
const sharp = require("sharp");

// Supabase 연결 설정
const supabaseUrl = "https://lxziyihbxcoatqaarfur.supabase.co";
const supabaseKey =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx4eml5aWhieGNvYXRxYWFyZnVyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTQyODAwNDAsImV4cCI6MjAyOTg1NjA0MH0.I2ZbK3F-c3kxaRczyAx7zVv1xv3YXLJk-nr5CY2W3j4";
const supabase = createClient(supabaseUrl, supabaseKey);

(async () => {
  for (let i = 2033; i <= 3120; i++) {
    const url = `${supabaseUrl}/storage/v1/object/public/labeled_image/images/${i}.jpeg`;
    const { data, error } = await supabase
      .from("labeled_image")
      .insert([{ id: i, image: url }])
      .select();
  }
})();
