// Reuben Thorpe (2016), CodeEval [Poker Hands v1.1]
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>


void get_highest_score_in_hand(int hand[5][2], int score[2], int num_seq[5]);
void n_of_a_kind(int num_seq[5], int n_of_kind[2], int* n_of_kind_weight);
const char* compare_poker_hands(int l_hand[5][2], int r_hand[5][2]);
void get_hands(FILE* in_file, int l_hand[5][2], int r_hand[5][2]);
void convert_to_numeric(char parse_hand[5][3], int hand[5][2]);
void get_num_sequence(int hand[5][2], int num_seq[5]);
void count_types_in_hand(int hand[5][2], int* types);
int cmpfunc (const void * a, const void * b);
bool is_hand_sequential(int num_seq[5]);
int get_max_id(int num_seq[5]);
int name_to_num(char name);
int min(int num_seq[5]);
int max(int num_seq[5]);
int sum(int num_seq[5]);


int main (int argc, const char* argv[]) {
  FILE* in_file = fopen(argv[1], "r");
  int l_hand[5][2], r_hand[5][2];

  while (!feof(in_file)) {
    get_hands(in_file, l_hand, r_hand);
    printf("%s\n", compare_poker_hands(l_hand, r_hand));
  }
  return(0);
}


const char* compare_poker_hands(int l_hand[5][2], int r_hand[5][2]) {
  // Comapare two poker hands and decide which one wins!
  int l_score[2], r_score[2], l_num_seq[5], r_num_seq[5], types;

  int max_l, max_r;

  get_highest_score_in_hand(l_hand, l_score, l_num_seq);
  get_highest_score_in_hand(r_hand, r_score, r_num_seq);

  if (l_score[0] > r_score[0]) return("left");

  else if (r_score[0] > l_score[0]) return("right");

  else {

    if (l_score[1] > r_score[1]) return("left");

    else if (r_score[1] > l_score[1]) return("right");

    else {

      while (max(l_num_seq) != 0) {
        max_l = max(l_num_seq);
        max_r = max(r_num_seq);

        if (max_l > max_r) return("left");

        else if (max_r > max_l) return("right");

        else {
          l_num_seq[get_max_id(l_num_seq)] = 0;
          r_num_seq[get_max_id(r_num_seq)] = 0;
        }
      }
      return("none");
    }
  }
}


void get_highest_score_in_hand(int hand[5][2], int score[2], int num_seq[5]) {
  // Generate the highest achivable score by a poker hand.
  int types, n_of_kind_weight, n_of_kind[2] = {0};

  get_num_sequence(hand, num_seq);
  count_types_in_hand(hand, &types);
  n_of_a_kind(num_seq, n_of_kind, &n_of_kind_weight);


  if (types == 1) {
    if (is_hand_sequential(num_seq)) {
      if (min(num_seq) == 10) {
        // Royal Flush
        score[0] = 9;
        score[1] = 0;
        return;
      }
      else {
        // Straight Flush
        score[0] = 8;
        score[1] = sum(num_seq);
        return;
      }
    }
    else {
      // Flush
      score[0] = 5;
      score[1] = sum(num_seq);
      return;
    }
  }

  else if (types == 4 && (n_of_kind[0] == 4 || n_of_kind[1] == 4)) {
    // Four of a Kind
    score[0] = 7;
    score[1] = n_of_kind_weight;
    return;
  }

  else if (is_hand_sequential(num_seq)) {
    // Straight
    score[0] = 4;
    score[1] = sum(num_seq);
  }

  else if (types >= 3 && (n_of_kind[0] == 3 || n_of_kind[1] == 3)) {
    if (n_of_kind[0] == 2 || n_of_kind[1] == 2) {
      // Full House
      score[0] = 6;
      score[1] = n_of_kind_weight;
      return;
    }
    else {
      // Three of a Kind 3
      score[0] = 3;
      score[1] = n_of_kind_weight;
      return;
    }
  }

  else if (types >= 2 && (n_of_kind[0] == 2 || n_of_kind[1] == 2)) {
    if (n_of_kind[0] == 2 && n_of_kind[1] == 2) {
      // Two Pairs
      score[0] = 2;
      score[1] = n_of_kind_weight;
      return;
    }
    else {
      // One Pair
      score[0] = 1;
      score[1] = n_of_kind_weight;
      return;
    }
  }

  else {
    score[0] = 0;
    score[1] = max(num_seq);
    return;
  }

}


void get_num_sequence(int hand[5][2], int num_seq[5]) {
  // Get all numeric values of cards in a hand disregarding type.
  for (int i = 0; i < 5; i++) num_seq[i] = hand[i][0];
  qsort(num_seq, 5, sizeof(int), cmpfunc);
}


int min(int num_seq[5]) {
  // Get the minimum from a numeric list.
  int min = num_seq[0];

  for (int i = 1; i < 5; i++) {
    if (num_seq[i] < min) min = num_seq[i];
  }
  return(min);
}


int max(int num_seq[5]) {
  // Get the maximum from a numeric list.
  int max = num_seq[0];

  for (int i = 1; i < 5; i++) {
    if (num_seq[i] > max) max = num_seq[i];
  }
  return(max);
}


int get_max_id(int num_seq[5]) {
  // Get the id of the maximum value from a numeric list.
  int max = num_seq[0];
  int max_id = 0;

  for (int i = 1; i < 5; i++) {
    if (num_seq[i] > max) {
      max = num_seq[i];
      max_id = i;
    }
  }
  return(max_id);
}


int sum(int num_seq[5]) {
  // Sum the values in a numeric list.
  int sum = 0;

  for (int i = 0; i < 5; i++) sum += num_seq[i];

  return(sum);

}


void count_types_in_hand(int hand[5][2], int* types) {
  // Count the amount of distinct types in a poker hand.
  int j, i;
  *types = 0;

  for(i = 0; i < 5; i++) {

    for (j=0; j<i; j++){
      if (hand[i][1] == hand[j][1]) break;
    }

    if (i == j) *types += 1;
  }
}


void n_of_a_kind(int num_seq[5], int n_of_kind[2], int* n_of_kind_weight) {
  // Abstract function to calculate the occurence of repeat cards.
  int j = 0;
  *n_of_kind_weight = 0;
  int prev = num_seq[0];
  int count = 1;

  for (int i = 1; i < 5; i++)
  {
    if (num_seq[i] == prev) count++;
    else
    {
      if (count > 1) {
        n_of_kind[j++] = count;
        *n_of_kind_weight += count * prev;
      }
      prev = num_seq[i];
      count = 1;
    }
  }

  if (count > 1) {
    n_of_kind[j++] = count;
    *n_of_kind_weight += count * prev;
  }

}


bool is_hand_sequential(int num_seq[5]) {
  // Determin if a numeric sequence can be sequential.
  for (int i = 1; i < 5; i++) {
    if (num_seq[i-1] != (num_seq[i] - 1)) return(false);
  }

  return(true);

}


void get_hands(FILE* in_file, int l_hand[5][2], int r_hand[5][2]) {
  // Parse CodeEval problem set Poker Hands into a usable format.
  char parse_l_hand[5][3], parse_r_hand[5][3];

  for (int i = 0; i < 5; i++) {
    fscanf(in_file, "%s ", parse_l_hand[i]);
  }

  for (int i = 0; i < 4; i++) {
    fscanf(in_file, "%s ", parse_r_hand[i]);
  }
  fscanf(in_file, "%s\n", parse_r_hand[4]);

  convert_to_numeric(parse_l_hand, l_hand);
  convert_to_numeric(parse_r_hand, r_hand);

}


void convert_to_numeric(char parse_hand[5][3], int hand[5][2]) {
  // Encode string formated card values into numeric representation.
  for (int i = 0; i < 5; i++) {
    if (isdigit(parse_hand[i][0])) hand[i][0] = parse_hand[i][0] - '0' ;
    else hand[i][0] = name_to_num(parse_hand[i][0]);

    if (isdigit(parse_hand[i][1])) hand[i][1] = parse_hand[i][1] - '0' ;
    else hand[i][1] = name_to_num(parse_hand[i][1]);
  }
}


int name_to_num(char name) {
  // Mapping for string values of cards to numeric values.
  switch(name) {

    // Royal name converstion
    case 'T' : return(10);
    case 'J' : return(11);
    case 'Q' : return(12);
    case 'K' : return(13);
    case 'A' : return(14);

    // Type converstion
    case 'C' : return(0);
    case 'D' : return(1);
    case 'H' : return(2);
    case 'S' : return(3);
  }
}

int cmpfunc (const void * a, const void * b) {
  // Computation function for the qsort algorithm.
  return ( *(int*)a - *(int*)b );
}
